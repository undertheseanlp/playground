import torch
from transformers import AutoModel, AutoTokenizer

bert_model = AutoModel.from_pretrained("vinai/phobert-base")

# For transformers v4.x+:
tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base")
# vocabs = list(tokenizer.vocab)
# For transformers v3.x:
# tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base")
vocabs = list(tokenizer.encoder)
# INPUT TEXT MUST BE ALREADY WORD-SEGMENTED!
lines = [
    "Tôi là sinh_viên trường đại_học Công nghệ .",
    "Tôi là sinh_viên trường đại_học Công_nghệ.",
    "Tôi là sinh_viên trường đại_học Công_nghệ .",
    "Tôi là sinh viên trường đại_học Công_nghệ .",
    'Tôi sinh ngày 23/11/2019'
]


class PhoBertEmbeddings:
    _model = None
    _tokenizer = None


for line in lines:
    print(line)
    input_id = tokenizer.encode(line, add_special_tokens=True)
    tokens = [(vocabs[i], i) for i in input_id]
    input_ids = torch.tensor([input_id])
    print(tokens)
    with torch.no_grad():
        features = bert_model(input_ids)  # Models outputs are now tuples
        print("F[0]:", features[0].shape)
        print("F[1]:", features[1].shape)
    print('\n')
