[![Code Climate](https://codeclimate.com/repos/55394aa2e30ba00af8001be9/badges/8ee3783737be9e27c1f0/gpa.svg)](https://codeclimate.com/repos/55394aa2e30ba00af8001be9/feed) 
[![Build Status](https://travis-ci.org/rafaharo/athento-imaging.svg?branch=master)](https://travis-ci.org/rafaharo/athento-imaging) 
[![Coverage Status](https://coveralls.io/repos/rafaharo/athento-imaging/badge.svg)](https://coveralls.io/r/rafaharo/athento-imaging)

# Athento-Imaging

Athento-Imaging is a Python library developed using OpenCV to improve OCR in
documents. Among the documents tested using this library are: passports, bills,
delivery notes, budgets, and other common documents.

You can check everything out in the [Athento-Imaging Summary.](docs/SUMMARY.md)

The quality of the output and it's OCR performance will depend on:

- The quality of the source document, as the quality value increases so does 
the OCR.
- The amount of noise in the document and it's position.
- The presence and position of the document's watermarks.
- The colour of the document. Clear colours are easier to remove than darker 
colours due to the proximity of the pixel values between the background and 
the text.
- Your personal experience in image transformation, as you might need to 
perform  a combination of operations or change the parameters values 
significantly.
