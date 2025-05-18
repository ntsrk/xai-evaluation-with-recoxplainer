# recoXplainer xai-evaluation

## Install

### Pre-requirements
The following toolkits are necessary: 
- conda
- git

### Clone and environment set-up
Clone the repo:

```buildoutcfg
git clone https://github.com/ntsrk/xai-evaluation-with-recoxplainer.git
```

Create environment on conda:

```buildoutcfg
conda create -n recoxplainer python=3.6 
```

RecoXplainer was developed with python 3.6. 
Activate the new environment:

```buildoutcfg
conda activate recoxplainer
```

### Dependencies

Install torch as explained in https://pytorch.org/, we are using the version without CUDA.

When torch is installed navigate to the folder where you cloned the library and run:

```buildoutcfg
pip install -r requirements.txt
```
This command will install all the dependencies.
Next, install the _recoxplainer_:
```buildoutcfg
pip install -e .
```
And finally run the notebooks:

```buildoutcfg
jupyter notebook
```


