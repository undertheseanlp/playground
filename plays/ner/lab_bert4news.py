import torch
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("NlpHUST/vibert4news-base-cased")
bert_model = AutoModel.from_pretrained("NlpHUST/vibert4news-base-cased")

lines = [
    "Tôi là sinh viên trường Bách Khoa Há Nội .",
    "Tôi là sinh viên trường Bách Khoa Hà Nội .",
]
vocabs = list(tokenizer.vocab)

for line in lines:
    input_id = tokenizer.encode(line, add_special_tokens=True)
    tokens = [(vocabs[i], i) for i in input_id]
    print(tokens)
    att_mask = [int(token_id > 0) for token_id in input_id]
    input_ids = torch.tensor([input_id])
    att_masks = torch.tensor([att_mask])
    with torch.no_grad():
        features = bert_model(input_ids, att_masks)
        print("F[0]:", features[0].shape)
        print("F[1]:", features[1].shape)
