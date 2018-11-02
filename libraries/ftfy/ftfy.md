Fixes Text For You ([ftfy][home])
=================================

**ftfy** fixes Unicode that’s broken in various ways.

The goal of ftfy is to take in bad Unicode and output good Unicode, for use in your Unicode-aware code. 
This is different from taking in non-Unicode and outputting Unicode, which is not a goal of ftfy. It also isn’t designed to 
protect you from having to write Unicode-aware code. ftfy helps those who help themselves.

Of course you’re better off if your input is decoded properly and has no glitches. But you often don’t have any control 
over your input; it’s someone else’s mistake, but it’s your problem now.

ftfy will do everything it can to fix the problem.

Also, keep in mind Joel Spolsky's great [Unicode character set article][joel-unicode] to avoid causing Unicode problems 
for others.


Installation
------------
```console
$ pip3 install ftfy
```


Usage
-----
```Python
import ftfy
```

See the [docs][home] for full usage instructions. Most useful examples are:

- Just fix the text  
  ```Python
  >>> ftfy.fix_text("doesnâ€™t")
  "doesn't"
  ```
- Explain each character  
  ```Python
  >>> ftfy.explain_unicode("doesnâ€™t")
  U+0064  d       [Ll] LATIN SMALL LETTER D
  U+006F  o       [Ll] LATIN SMALL LETTER O
  U+0065  e       [Ll] LATIN SMALL LETTER E
  U+0073  s       [Ll] LATIN SMALL LETTER S
  U+006E  n       [Ll] LATIN SMALL LETTER N
  U+00E2  â       [Ll] LATIN SMALL LETTER A WITH CIRCUMFLEX
  U+20AC  €       [Sc] EURO SIGN
  U+2122  ™       [So] TRADE MARK SIGN
  U+0074  t       [Ll] LATIN SMALL LETTER T
  ```
- Run a single decode pass and explain what it did (good for guessing a single bad encoding)  
  ```Python
  >>> ftfy.fixes.fix_one_step_and_explain("doesnâ€™t")
  ('doesn’t', [('encode', 'sloppy-windows-1252', 0), ('decode', 'utf-8', 0)])
  ```




[home]: https://ftfy.readthedocs.io/en/latest/#
[joel-unicode]: https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/
