## Step 1
1. If Anaconda base environment is not activated in powershell terminal in vs code in any folder ther use this command:
- `conda init powershell`
2. if success then you will see:
- `no change   ---`
- `modified    ---`

## Step 2
- `conda activate base` (for activate anaconda base environment)

## Step 3
- `python --version`

## Step 4
- `conda info`

## Step 5
- `conda env list`

## Step 6
- `conda create --name py310 python=3.10`

## Step 7
- `conda env list`

## Step 8
- `conda activate py310`

## Step 9
- `conda install seaborn`

## Step 10
- `conda deactivate`

## Step 11
- `conda config --set auto_activate_base false`