echo -e "[status] Text Analysis\n"
cd analysis && python3 text_analysis.py && cd ..
echo -e "\n"
echo -e "[status] Nltk Analysis\n"
python3 ./analysis/nltk_analysis.py
echo -e "\n"
echo -e "[status] Twitter Analysis\n"
python3 ./analysis/twitter_analysis.py
echo -e "\n"
