# Agent Notes

This is a Jekyll portfolio site. The header navigation is generated from
`site.pages` in `_includes/navigation.html`.

Important gotcha: Markdown files placed at the repository root can be treated as
Jekyll pages and may appear in the header menu if they have a title. Keep
internal documentation in ignored underscore folders such as `_maintenance/`, or
explicitly exclude root-only files from the navigation template.

Use `_pages/` for intentional top-level site pages.
