# Agent Notes

This is a Jekyll portfolio site. The header navigation is generated from
`site.pages` in `_includes/navigation.html`.

Important gotcha: Markdown files placed at the repository root can be treated as
Jekyll pages and may appear in the header menu if they have a title. Keep
internal documentation in ignored underscore folders such as `_maintenance/`, or
explicitly exclude root-only files from the navigation template.

Use `_pages/` for intentional top-level site pages.

Header controls live in `_config.yml`:

```yaml
header:
  show_logo: false
  show_search: false
```

`show_logo: false` hides the header logo/title area. If `show_logo` is enabled
and `logo:` is empty, the header falls back to rendering `site.title` as text.
`show_search: false` hides the search trigger. When both are false, the header
adds state classes and `_sass/3-modules/_header.scss` centers the desktop nav
while keeping the mobile menu icon aligned to the right.

Project cards and grids are rendered by `_includes/project-grid.html` (grid +
optional client-side filters) and `_includes/article-content.html` (one card).
Homepage filter buttons come from `project_filters` in `_config.yml`; a button
is only shown when at least one post has one of its tags. The homepage hero
text comes from `hero.eyebrow`, `hero.title`, `hero.pitch`, `hero.subline_lead` and
`hero.subline` (markdown, piped through `markdownify`, so `**bold**` and `- ` bullets render).
