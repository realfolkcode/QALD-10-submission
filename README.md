# QALD-10-submission

## Usage

1. Retrieve questions from the test set via `retrieve_questions.py` script (`qald_10.json` should be in the same directory as the script).

2. Translate questions from other languages to English via `t5_translation.ipynb`.

3. Run `KEQA_inference.ipynb` notebook to generate predictions using KEQA framework. Rename the file with predictions in the following manner: `en_prediction.txt` for EN questions, `ru_questions.txt` for RU questions, `de_questions.txt` for DE questions and `ze_questions.txt` for ZH questions.

4.

5. Finally, generate submissions for all languages via `generate_submission.ipynb`.
