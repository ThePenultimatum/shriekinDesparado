# Project Title

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python 2.7 or 3.6
TensorFlow
NumPy

If training:
Ideally GPUs that TensorFlow can take advantage of
Otherwise, time. Training can take a while.

### Installing

Clone or fork this repo.

```bash
git clone https://github.com/ThePenultimatum/shriekinDesparado.git
```

Enter the directory. Ensure the data you want to train on is in the chatbotData directory. Or you can use the default hyperparameters just to test immediately.

Data will be in the format of two files for training.
prompts.txt and responses.txt
Each newline separated prompt and response in these files must be in order such that line 0 in each file corresponds to a prompt and response pair. If this is not the case, then the data will not be trained on properly.

Run train.py
```bash
python train.py
```

Then run eval.py
```bash
python eval.py
```

This will bring up a command line prompt for you to type something into the command line and hit enter. This will submit your text to the trained model for prediction and will return a response predicted based on the training data.

## Deployment

## Built With

## Contributing

## Versioning

## Authors

* **Yuchen Wang** - *Initial work* - [yuchnw](https://github.com/yuchnw)
* **Mark Dyehouse** - *Initial work* - [ThePenultimatum](https://github.com/ThePenultimatum)

See also the list of [contributors](https://github.com/ThePenultimatum/shriekingDesparado/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Google Brain team from the paper "Attention is All You Need" who originally detailed the Transformer model
* GitHub user [Kyubyong Park](https://github.com/Kyubyong) for his work on developing a usable [Transformer](https://github.com/Kyubyong/transformer) in Python
* Dr. Han Liu of Northwestern University

