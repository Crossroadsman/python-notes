TDD
===

Consider the following test (of a Django view):

```python
    # First we mock out the List class to get access to any lists that
    # might be created by the view.
    # This requires us to also mock out ItemForm, since the real ItemForm
    # can't use a mock object as the foreign key for the Item it will want
    # to create (and so would raise an error on `form.save()`)
    #
    # the method signature needs to have the mocks injected in the reverse
    # order to which they are patched.
    @patch('lists.views.List')
    @patch('lists.views.ItemForm')
    def test_list_is_linked_to_owner_if_user_authenticated(
        self, mockItemFormClass, mockListClass
    ):
        # the list instance that the view will have access to is the
        # return value of the mocked List class (thus we will be able
        # to make assertions on the attributes set on the mock class
        # by the view, in this case `owner`)
        mock_list = mockListClass.return_value

        # Without the following line we get a long error, ending with
        # TypeError: quote_from_bytes() expected bytes
        #
        # This is because our view is going to call get_absolute_url on
        # List (or in this case, our mocked version of List).
        # Django needs get_absolute_url to return a string (which it
        # can convert into bytes) but calling it on a mock returns
        # another mock, which is not a string.
        # Thus by pre-seeding a return value, the subsequent call
        # will get this string, instead of a mock.
        #mockListClass().get_absolute_url.return_value = 'fake_url'
        mock_list.get_absolute_url.return_value = 'fake_url'
        # strictly speaking, this test only confirms that we create
        # an value for `owner`. It doesn't test the sequence (i.e.,
        # that we create `owner` before saving the List object and
        # not the other way round).
        # Note that this would be trivial to prove if we weren't using
        # mocks, so we need to be alert to things that would be obvious
        # in a fully-implemented version of our code but aren't
        # certain while we are using test doubles.
        # One approach to address this when using mocks is to create
        # a function to act as a spy and attach it to the mocked object
        # representing the real object's method we want to spy on (in this
        # case `save`)
        def check_owner_assigned():
            self.assertEqual(mock_list.owner, user)
        # note that the sequence of code is significant when using the spy:
        # - we need to assign the side effect before the function that
        #   would trigger the side effect is called (this might seem too
        #   obvious to mention, but it is very easy to overlook)
        mock_list.save.side_effect = check_owner_assigned

        user = User.objects.create(email='a@b.com')
        # `force_login()` is the Django test suite's way of simulating the
        # effect of logging a user into the site. It should be used in
        # place of `login()` when a test requires a user be logged in and
        # the details of how a user logged in aren't important.
        self.client.force_login(user)

        # the following line will call the `new_list` view. In the
        # view, it will attempt to create a new ItemForm instance and
        # populate it with the POST data.
        # This will be intercepted by the mockItemFormClass and a magic
        # mock instance will be created instead.
        # Any call to a method on the mock will create a new mock object
        # thus calling `is_valid()` will create a new `is_valid` mock
        # object on MockItemFormClass.
        # Because it has the (mocked) `is_valid`, it is truthy, which
        # enables the True branch of the if statement to be executed.
        # This then enables us to create the mock List item, which was
        # our original mocking intent (so we could pretend that List
        # has an `owner` attribute).
        self.client.post('/lists/new', data={'text': 'new item'})

        # We've moved the real assertion (that user now has an owner)
        # into the spy. However, the spy will only run (and thus the
        # assertion will only be fired) if the mocked method we attached
        # the spy to actually gets called. So we also need to assert
        # that the spied method was called:
        # (assert_called_once and assert_called_once_with are assertion
        # methods provided with Mock:
        # https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_with
        # )
        mock_list.save.assert_called_once()
```

This is one long, ugly test (even with all the comments removed):
```python
    @patch('lists.views.List')
    @patch('lists.views.ItemForm')
    def test_list_is_linked_to_owner_if_user_authenticated(
        self, mockItemFormClass, mockListClass
    ):
        mock_list = mockListClass.return_value

        mock_list.get_absolute_url.return_value = 'fake_url'
        def check_owner_assigned():
            self.assertEqual(mock_list.owner, user)
        mock_list.save.side_effect = check_owner_assigned

        user = User.objects.create(email='a@b.com')
        self.client.force_login(user)

        self.client.post('/lists/new', data={'text': 'new item'})

        mock_list.save.assert_called_once()
```
Observe that we have tons of setup, creating multiple mocked classes and a spy.

This is our test telling us that we need to refactor, and specifically we need
to refactor our application, not just our test.

In this case, we are testing a view, and if we need to do all this setup and
mocking, it should be clear to us that our view is doing too much. In this
case the view is:
- creating a form;
- creating a new List object;
- deciding whether to save an owner for the list.

Thus we can refactor by moving some of this application logic outside the view.
Both the List creation and making decisions about saving a user could be
performed by the Form.
