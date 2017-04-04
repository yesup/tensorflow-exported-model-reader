import fire

if __name__ == "__main__":
    from yesup.tensorflow.tools.exported_model_reader import Reader

    fire.Fire(Reader)