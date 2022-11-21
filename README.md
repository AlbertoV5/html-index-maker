# HTML Index Maker

Scrape local HTML files and generate an index.

## Usage

```shell
python -m html-index-maker -i ./resources -f .html -o ./data.json
```

This will call the module on the resources directory, look for html files and store the result in a given json file.

## Supported Reading Formats

- HTML
- ORG

## Supported Writing Formats

- JSON
- JS
- ORG
- MARKDOWN