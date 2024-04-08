# pantsanity

[For now] A sanity check for the call-by-syntax migration. 

The call-by-syntax migration affects almost every file in the Python portion of the Pants code, but the `migrate...` goal only migrates rules for active backends. And then, in order to figure out whether the code still works, we need to ensure the migrated code is hit - either by tests, or at runtime, or both.

Since the Pants repo is so large and intertwined, repeatedly running goals and tests on the entire repo with a lot of active backends is slow. The goal of this repo is to (eventually) activate most/all backends and run as many goals as possible, on a per-language "hello world" project. Since the actual source code is almost non-existent, running sanities should be pretty quick.

As a small bonus, it's trivial to compare the output of migrated Pants against a release or another non-migrated branch. 

## Usage

```bash
pants sanity ::

# From sources:
PANTS_SOURCE=../wherever-your-pants-repo-is pants sanity ::
```
