# GSVD
Generalized Smart Contract Vulnerability Dataset 

广义智能合约漏洞数据集



<br>

</br>

## Timeline & Work

- **Timeline:**
  - Phase1: 2021.10 ~ 2022.06
  - Phase2: TBD (After paper work)

- **Work:**

  - Phase1:

    Platform: BSC + Polygon

    Scale: **153** contracts for Minor + **42202** contracts for Major

    Tools: Slither + Manticore + Mythril

  - Phase2:

    Platform: BSC + Polygon + *Avalanche* + *Fantom* + TBD

<br>

</br>

## Composition

**GSVD<sup>Minor</sup>**   &   **GSVD<sup>Major</sup>**

<br></br>

- GSVD<sup>Minor</sup>: Small Dataset Focused on Vulnerabilities

  A class of real-world smart contract datasets containing typical vulnerabilities.

  - GSVD<sup>Minor</sup><sub>BSC</sub>: 97
  - GSVD<sup>Minor</sup><sub>Polygon</sub>: 56

- GSVD<sup>Major</sup>: Large Dataset Focused on Real-world Environments

  A dataset that consistently integrates a large number of deployed smart contracts in real-world chains.

  - GSVD<sup>Major</sup><sub>BSC</sub>: 41602
  - GSVD<sup>Major</sup><sub>Polygon</sub>: 10600

<br>

</br>

## Utilization

**Linux**/**Win**

**Anaconda** is highly recommended and python3.7 is a rather stable and compatible version. 

<br>

</br>

After practive, we see the version number below as the stablest and most user-friendly version of each tool.

| Tool Name | Version |
| --------- | ------- |
| Slither   | 0.8.2   |
| Manticore | 0.3.6   |
| Mythril   | 0.22.43 |

With Intel 10th i7 processor and 16GB RAM, the execution time of each tool are shown below.

| Num  | ToolName  | Avg Exec Time | Total Exec Time |
| ---- | --------- | ------------- | --------------- |
| 1    | Slither   | 0 m 9 s       | 0 h 22 m 31 s   |
| 2    | Manticore | 16 m 24 s     | 41 h 54 m 2 s   |
| 3    | Mythril   | 1 m 42 s      | 4 h 15 m 6 s    |

<br>

</br>

Install the scripts framework environment:

~~~bash
conda install requirements.txt
~~~

Collect contract info from third-party websites(Change the address in crawl.py):

~~~bash
~~~

Classify the collected contracts(Change the address in classification.py):

~~~bash
~~~

