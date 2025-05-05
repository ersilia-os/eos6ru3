# WHALES similarity search on 600k molecules from Q-Mug

Search Q-Mug based on WHALES descriptors. Q-Mug is a subset of 600k bioactive molecules from ChEMBL. Three conformers are given for each molecule. WhALES is a simple descriptor useful for scaffold hopping.

This model was incorporated on 2024-04-22.

## Information
### Identifiers
- **Ersilia Identifier:** `eos6ru3`
- **Slug:** `whales-qmug`

### Domain
- **Task:** `Sampling`
- **Subtask:** `Similarity search`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Similarity`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `100`
- **Output Consistency:** `Fixed`
- **Interpretation:** The top 100 most similar molecules are returned, based on WHALES descriptors. 3D conformer generation is done internally.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| smiles_00 | string |  | Similar molecule index 0. This molecule is from the QMUG database and similarity is based on WHALES descriptors |
| smiles_01 | string |  | Similar molecule index 1. This molecule is from the QMUG database and similarity is based on WHALES descriptors |
| smiles_02 | string |  | Similar molecule index 2. This molecule is from the QMUG database and similarity is based on WHALES descriptors |
| smiles_03 | string |  | Similar molecule index 3. This molecule is from the QMUG database and similarity is based on WHALES descriptors |
| smiles_04 | string |  | Similar molecule index 4. This molecule is from the QMUG database and similarity is based on WHALES descriptors |
| smiles_05 | string |  | Similar molecule index 5. This molecule is from the QMUG database and similarity is based on WHALES descriptors |
| smiles_06 | string |  | Similar molecule index 6. This molecule is from the QMUG database and similarity is based on WHALES descriptors |
| smiles_07 | string |  | Similar molecule index 7. This molecule is from the QMUG database and similarity is based on WHALES descriptors |
| smiles_08 | string |  | Similar molecule index 8. This molecule is from the QMUG database and similarity is based on WHALES descriptors |
| smiles_09 | string |  | Similar molecule index 9. This molecule is from the QMUG database and similarity is based on WHALES descriptors |

_10 of 100 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos6ru3](https://hub.docker.com/r/ersiliaos/eos6ru3)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos6ru3.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos6ru3.zip)

### Resource Consumption
- **Model Size (Mb):** `301`
- **Environment Size (Mb):** `1011`


### References
- **Source Code**: [https://github.com/ETHmodlab/scaffold_hopping_whales](https://github.com/ETHmodlab/scaffold_hopping_whales)
- **Publication**: [https://link.springer.com/protocol/10.1007/978-1-0716-1209-5_2](https://link.springer.com/protocol/10.1007/978-1-0716-1209-5_2)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2021`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-only](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos6ru3
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos6ru3
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
