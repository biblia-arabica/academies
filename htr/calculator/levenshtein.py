from Levenshtein import distance

ground_truth_filename = "../transcriptions/OxfordLaudOr258/txt/OxfordLaudOr258_033-034-Unvocalized_manual,_corrected_011-012-transcription-rasm-no-dividers-no-spaces.txt"
with open(ground_truth_filename, 'r', encoding='utf8') as ground_truth_file:
    ground_truth = ground_truth_file.read()

htr_filename = "../transcriptions/OxfordLaudOr258/txt/OxfordLaudOr258_033-034-kraken-lmu_Ox258_clean08_best-model-rasm-no-dividers-no-spaces.txt"
with open(htr_filename, 'r', encoding='utf8') as htr_file:
    htr = htr_file.read()

ground_truth_chars = len(ground_truth)
distance = distance(ground_truth, htr)
cer = distance/ground_truth_chars
cer_norm = distance/(distance + ground_truth_chars)
accuracy = (1 - (cer_norm))*100

print("GT Length\t", "L Distance\t", "CER\t", "CER Normalized\t","Accuracy")
print(ground_truth_chars, "\t\t", distance, "\t\t", round(cer, 3), "\t", round(cer_norm, 3), "\t\t", round(accuracy, 1))