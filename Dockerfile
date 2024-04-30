FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install rdkit==2023.3.1
RUN pip install pandas==1.3.5
RUN pip install joblib==1.3.2
RUN pip install scikit-learn==1.0.2
RUN conda install -c conda-forge xorg-libxrender xorg-libxtst

WORKDIR /repo
COPY . /repo
