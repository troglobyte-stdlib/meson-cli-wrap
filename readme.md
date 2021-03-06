# Meson CLI wrapper

## overview

* * *

There are two different ways of invoking Meson.
First, you can run it directly from the source
tree with the command `/path/to/source/meson.py`.
Meson may also be installed in which case the
command is simply `meson`. In this manual we only
use the latter format for simplicity.

Meson is invoked using the following syntax: 

`meson [COMMAND] [COMMAND_OPTIONS]`

This package wraps the commands into usable methods
for your use case.

## tooling

* * *

The targeted audience we are building for is **Windwos 10**, **MacOSX**, **ChromeOS**, and
**Linux** users. This project uses [Python](https://www.python.org/) `3.8.x` and newer.

## Test, Install and Run

* * *

We should make sure the test run with no failed test cases:

```console
python3 -m pip install -r requirements.txt
python3 -m pytest test/run_tests.py
```

Installing should be easy. We install the application like so:

```console
python3 setup.py install
```

And finally we can use this in that cool application:

## contact

If you want to contact me and have a few questions
regarding the solutions in the programming you can write
me a letter, my Gmail is <michaelbrockus@gmail.com>.

You may find that I have some social media platforms
in which you can follow me. [LinkedIn](https://www.linkedin.com/in/michael-brockus), [Facebook](https://facebook.com/michael.brockus.555), and [Instagram](https://instagram.com/troglobyte_coder/)
