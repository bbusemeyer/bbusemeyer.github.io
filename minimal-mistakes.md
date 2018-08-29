# Notes for working with minimal-mistakes theme.

When using Bundler to manage gems you’ll want to run Jekyll using `bundle exec jekyll serve` and `bundle exec jekyll build`.

Doing so executes the gem versions specified in `Gemfile.lock`. Sure you can test your luck with a naked `jekyll serve`, but I wouldn’t suggest it. 
A lot of Jekyll errors originate from outdated or conflicting gems fighting with each other. 
So do yourself a favor and just use Bundler.
