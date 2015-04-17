# Athento-imaging

Athento-Imaging is a package developed using Python and OpenCV to improve OCR in
documents. Among the documents tested using this package are: passports, bills,
delivery notes, budgets, and other common documents.

This package includes several functions to transform images:

- Remove coloured background.
- Remove "salt and pepper" noise.
- Line detection in documents (two approachs).
- Remove lines in documents.
- Simple line analysis (which lines are horizontal and vertical, distance between lines, etc.
- Template matching improved using pyramid transformations.


You can check everything out here: [Athento-Imaging Summary](<docs/SUMMARY.md>)

The quality of the output and it's OCR performance will depend on:

- The quality of the source document, as the quality value increases so does the OCR.
- The amount of noise in the document and where it's located.
- The location of the document's watermarks (if any).
- The colour of the document. Clear colours are easier to remove than darker colours due to the proximity of the pixel values between the background and the text.
- Your personal experience in image transformation. As you might need to perform  a combination of operations or change the parameters values significantly.