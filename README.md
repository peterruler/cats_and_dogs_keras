# cats_and_dogs_keras
python keras cats and dogs classification

https://keras.io/examples/vision/image_classification_from_scratch/

# install tensorflow
https://www.youtube.com/watch?v=5DgWvU0p2bk

Explanation: https://github.com/jeffheaton/t81_558_deep_learning/blob/master/install/tensorflow-install-mac-metal-jan-2023.ipynb

https://github.com/jeffheaton/t81_558_deep_learning/blob/master/install/tensorflow-install-mac-metal-jan-2023.ipynb

remove anaconda if previously installed

https://docs.anaconda.com/free/anaconda/install/uninstall/

`conda install anaconda-clean`

in a terminal run `anaconda-clean`

```
# The following are a few examples of how you may need to delete your Anaconda folder
rm -rf anaconda3
rm -rf ~/anaconda3
rm -rf ~/opt/anaconda3
```

install miniconda for macos m1 arm64 or suiting to your machine

```
# in a terminal run
python #enter
install platform
platform.platform() #enter
# outputs sth. like:
'macOS-13.4.1-arm64-arm-64bit'
```

`xcode-select --install`

`conda install -y jupyter`

`which jupyter`

` /Users/<USERNAME>/miniconda3/bin/jupyter notebook`

`conda deactivate` vs. (base) `activate pytorch`

`conda env create -f tensorflow-apple-metal.yml -n tensorflow`

`conda activate tensorflow`

`python -m ipykernel install --user --name tensorflow --display-name "Python 3.10 (tensorflow)"`

`jupyter notebook`

# keras

https://keras.io/examples/vision/image_classification_from_scratch/

`curl -O https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip`

`unzip -q kagglecatsanddogs_5340.zip`

`ls PetImages`

to get testdata register & download https://www.kaggle.com/competitions/dogs-vs-cats-redux-kernels-edition/data

`conda install pip` optional

`brew install pydot` did the job for me

 otherwise try `conda install pydot`

`conda install graphviz` did the job for me

# save model in keras

https://www.tensorflow.org/guide/keras/serialization_and_saving


don't call any of the two following command:
neither

`pip install tf-nightly keras-nightly`

nor

`pip install tfp-nightly`

# uninstall miniconda
 (in case yout damadged sth.)

```
conda activate your_conda_env_name
conda install anaconda-clean
anaconda-clean # add `--yes` to avoid being prompted to delete each one
rm -rf ~/miniconda3
vi ~/.bashrc
# -> Search for conda and delete the lines containing it
# -> If you're not sure if the line belongs to conda, comment it instead of deleting it just to be safe
source ~/.bashrc
```

# save & load model

I chose json serialisation, which works great.

Also save & load the models' weights as well.

https://machinelearningmastery.com/save-load-keras-deep-learning-models/
