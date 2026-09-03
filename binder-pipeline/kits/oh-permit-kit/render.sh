#!/bin/sh
# Render every kit PDF to PNG for visual review.
# pdftoppm zero-pads its output index to the width of the page count, so a
# document that grows from 9 to 10 pages starts writing fl1-01.png while the
# old fl1-1.png survives — and you end up reviewing a stale page. Wipe first.
set -e
cd "$(dirname "$0")"
rm -rf png && mkdir -p png
for f in out/oh-permit-kit/*.pdf; do
  b=$(basename "$f" .pdf | cut -d- -f1 | tr -d '.' | tr 'A-Z' 'a-z')
  pdftoppm -png -r 80 "$f" "png/$b"
done
ls png/
