# MDBook backend for Pants

> **Warning**
> 🚧 Very WIP plugin 🚧

This provides a tool for building mdbook targets with pants. There is currently a single very simple rule:

``` python
md_book(
    name="my-docs",
    sources=["book.toml", "src/*"],
)
```

| Argument | Meaning | Default value |
| --- | --- | --- |
| `name` | The target name | Same as any other target, which is the directory name |
| `sources` | Files included when building the book | `book.toml` and the `src` directory |
| `decsription` | A description of the target | `""` |
| `tags` | List of tags | `[]` |
