from underthesea.file_utils import DATASETS_FOLDER


class DPTagger:
    def __init__(self, name):
        self.name = name

    def tag(self, input, output):
        pass


class VLSP2020_DP_R1:
    def __init__(self):
        VLSP2020_DP_FOLDER = f'{DATASETS_FOLDER}/VLSP2020-DP-R1'
        train_file = f'{VLSP2020_DP_FOLDER}/DP-Package2.18.11.2020.txt'
        self.train = train_file

        test_file = f'{VLSP2020_DP_FOLDER}/VTB_400.txt'
        self.test = test_file
