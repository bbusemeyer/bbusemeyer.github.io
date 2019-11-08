# bbusemeyer.github.io

I'll try to keep this web site up-to-date with tips and notes that were useful to me in my numerical condensed matter physics research.

## Helpful tools for maintaining and editing this kind of website.

You can fork and edit this repo to get a copy of this web site for yourself!
That's what I did to [Ryan Levy](https://ryanlevy.github.io) (and of course the minimal-mistakes repo). 

- Important: when editing things, don't double `site/`, because that is overwritten with each compilation.
- If something doesn't update in the website, it's probably because you need to restart the server. I think this includes anything in `_config.yaml`.
- Check the Jekyll documentation for help adjusting the structure, organization, and defaults of the web site.
- Check the minimal-mistakes page for help only if that fails. His documentation is more professional-grade and Jekyl's is for noobs.

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
- Edit `_data/navigation.yml`. This changes the header of the home page.
- Added HTML: `_includes/archive-paper.html`. This HTML specifies how the papers page displays the information.
- Added `papers-archive.html` to `_pages/`. This will be the papers summary page.
- Added a MD file to `_papers/`. This adds a new papers post.
These settings are connected together through their permalink and their layout.
Make sure these are consistent.

### Other modifications.

- Modified font sizes with `_sass/minimal-mistakes/_archive.scss` and `_sass/minimal-mistakes/_page.scss`, which modifies properties of those page templates.

# TO DO.

- Fill in summaries of other papers.
