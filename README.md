# ChonBot auto discovery service


|![chonOS-Neighbors-capa](https://github.com/chon-group/dpkg-chonos-neighbors/assets/32855001/66f06c91-a113-42b6-a177-50015e176659)|
|:--:|
|ChonOS-Neighbors implements auto discovery of _Cognitive Hardware on Networks Operating System (chonOS)_ on the Local Area Network.|

## How to Install?
1) In a terminal run the commands below:

```console
echo "deb [trusted=yes] http://packages.chon.group/ chonos main" | sudo tee /etc/apt/sources.list.d/chonos.list
sudo apt update
sudo apt install chonos-neighbors
```

### DESCRIPTION

List of options and arguments:
|Argument|Description|
|-|-|
|___--list___|list of the discovered ChonBots in the local area network.|
|___--forget___|clean the list of discovered ChonBots.|
|___--start___|start the chonos-neighbors service.|
|___--stop___|stop the chonos-neighbors service.|

### EXAMPLE
![image](https://github.com/user-attachments/assets/cdfb2531-13a0-4f99-8a23-b65fc44054f8)



## COPYRIGHT
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />The ChonOS-Neighbors is part of the [_Cognitive Hardware on Network - IDE (ChonIDE)_](https://ide.chon.group) and is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>. The licensor cannot revoke these freedoms as long as you follow the license terms:

* __Attribution__ — You must give __appropriate credit__ like below:

Souza de Jesus, V., Mori Lazarin, N., Pantoja, C.E., Vaz Alves, G., Ramos Alves de Lima, G., Viterbo, J. (2023). An IDE to Support the Development of Embedded Multi-Agent Systems. In: Mathieu, P., Dignum, F., Novais, P., De la Prieta, F. (eds) Advances in Practical Applications of Agents, Multi-Agent Systems, and Cognitive Mimetics. The PAAMS Collection. PAAMS 2023. Lecture Notes in Computer Science(), vol 13955. Springer, Cham. [https://doi.org/10.1007/978-3-031-37616-0_29](https://www.researchgate.net/publication/372282731_An_IDE_to_Support_the_Development_of_Embedded_Multi-Agent_Systems)


<details>
<summary> Bibtex citation format</summary>

```
@InProceedings{chonIDE,
    doi="10.1007/978-3-031-37616-0_29"
    author="Souza de Jesus, Vinicius
    and Mori Lazarin, Nilson
    and Pantoja, Carlos Eduardo
    and Vaz Alves, Gleifer
    and Ramos Alves de Lima, Gabriel
    and Viterbo, Jose",
    editor="Mathieu, Philippe
    and Dignum, Frank
    and Novais, Paulo
    and De la Prieta, Fernando",
    title="An IDE to Support the Development of Embedded Multi-Agent Systems",
    booktitle="Advances in Practical Applications of Agents, Multi-Agent Systems, and Cognitive Mimetics. The PAAMS Collection",
    year="2023",
    publisher="Springer Nature Switzerland",
    address="Cham",
    pages="346--358",
    isbn="978-3-031-37616-0"
}

```
</details>
