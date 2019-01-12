from utils import create_input_files

if __name__ == '__main__':
    dataset_loc = "/mnt/win-F/deep-learning-data/cocoapi/"

    # Create input files (along with word map)
    create_input_files(dataset='coco',
                       karpathy_json_path=dataset_loc+'caption_datasets/dataset_coco.json',
                       image_folder=dataset_loc+'images/',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder=dataset_loc+'caption_output/',
                       max_len=20)
