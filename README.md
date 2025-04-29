# WHALES similarity search on 600k molecules from Q-Mug

Search Q-Mug based on WHALES descriptors. Q-Mug is a subset of 600k bioactive molecules from ChEMBL. Three conformers are given for each molecule. WHALES is a simple descriptor useful for scaffold hopping.

## Identifiers

* EOS model ID: `eos6ru3`
* Slug: `whales-qmug`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Generative`
* Output: `Compound`
* Output Type: `String`
* Output Shape: `List`
* Interpretation: The top 100 most similar molecules are returned, based on WHALES descriptors. 3D conformer generation is done internally.

## References

* [Publication](https://link.springer.com/protocol/10.1007/978-1-0716-1209-5_2)
* [Source Code](https://github.com/ETHmodlab/scaffold_hopping_whales)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos6ru3)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos6ru3.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos6ru3) (AMD64)

## Citation

If you use this model, please cite the [original authors](https://link.springer.com/protocol/10.1007/978-1-0716-1209-5_2) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a GPL-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!
