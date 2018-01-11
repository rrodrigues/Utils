

## Image Utils

### sips

* scale keep aspect ratio `sips -Z {max_dim} {files}`
* convert to format `sips {in_file}.{in_ext} -s format {out_ext}  --out {out_file}.{out_ext}`
  * with compression level `-s formatOptions 9`


## Rename files

### Remove part of the name
From [here](https://stackoverflow.com/a/24103055)

`for f in *.png; do mv "$f" "${f/_*_/_}" ; done`

where:
* "${f/_*_/_}" is an application of bash parameter expansion: the (first) substring matching pattern _*_ is replaced with literal _, effectively cutting the middle token from the name.