# bbusemeyer.github.io

I'll try to keep this web site up-to-date with tips and notes that were useful to me in my numerical condensed matter physics research.

## Helpful tools for maintaining and editing this kind of website.

You can fork and edit this repo to get a copy of this web site for yourself!
That's what I did to [Ryan Levy](https://ryanlevy.github.io) (and of course the minimal-mistakes repo). 

Important: when editing things, don't double `site/`, because that is overwritten with each compilation.

### Getting Jekyll set up.

Resources:
- [Jekyll website for more general details](https://jekyllrb.com/docs/).
- [Minimal mistakes information on dependencies](https://mmistakes.github.io/minimal-mistakes/docs/installation/#install-dependencies).

I did the following on Kubuntu 18.04:

```
sudo apt-get install ruby-dev gem 
gem install jekyll bundler # This takes some time.
bundle
```

Now `bundle exec jekyll serve` will allow you to run a [server at this location](http://127.0.0.1:4000).

### Editing blog posts.

TBA

### Adding papers.

TBA

### Making my `papers` page.

More information in the git log of this repo, but in short:

- Make a papers template.
- Added HTML to `_includes/archive-paper`.
- Added `papers-archive.html` to `_pages/`.
- Added a MD file to `_papers/`.

### Other modifications.

- Modified font sizes with `_sass/minimal-mistakes/_archive.scss` and `_sass/minimal-mistakes/_page.scss`, which modifies properties of those page templates.
