sentences=$1 #input name without .csv
folder=$2

mkdir $folder

python3 code/get_afinn_emotion.py ${sentences}.csv

mv ${sentences}_AFINN_Emotions.csv $folder

python3 code/get_connotation_emotions.py ${sentences}.csv lexicons/connotation_lexicon_a.0.1.csv

mv ${sentences}_Connotation_Emotions.csv $folder

python3 code/get_liwc_emotion.py ${sentences}.csv lexicons/LIWC2015_English_Flat.dic

mv ${sentences}_LIWC_Emotions.csv $folder

python3 code/get_mpqa_emotion.py ${sentences}.csv lexicons/subjclueslen1-HLTEMNLP05.tff

mv ${sentences}_MPQA_Emotions.csv $folder

python3 code/get_sentence_polarity.py $folder/${sentences}_polarity_liwc.csv liwc $folder/${sentences}_LIWC_Emotions.csv 
python3 code/get_sentence_polarity.py $folder/${sentences}_polarity_mpqa.csv mpqa $folder/${sentences}_MPQA_Emotions.csv 
python3 code/get_sentence_polarity.py $folder/${sentences}_polarity_afinn.csv afinn $folder/${sentences}_AFINN_Emotions.csv 
python3 code/get_sentence_polarity.py $folder/${sentences}_polarity_connotation.csv afinn $folder/${sentences}_Connotation_Emotions.csv 

python3 code/get_marked_sentences.py ${sentences}.csv

mv ${sentences}_indicators.csv $folder

python3 code/get_all_info.py $folder/${sentences}_polarity_liwc.csv $folder/${sentences}_polarity_mpqa.csv $folder/${sentences}_polarity_afinn.csv $folder/${sentences}_polarity_connotation.csv $folder/${sentences}_indicators.csv

mv all_info.csv $folder

mkdir $folder/supplemental_info/

mv $folder/${sentences}* $folder/supplemental_info


