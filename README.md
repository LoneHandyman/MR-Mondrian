# MR-Mondrian

### Implementation:
### PID-tree:
* **Description:**
The Partition Identifier (PID) Tree is a structure used in data anonymization to preserve the privacy of sensitive information. The PID Tree is constructed in a Breadth-First Manner (BFM) and is used for performing search and insertion operations.
* **Structure:**
The PID Tree consists of nodes that represent data partitions. Each node contains the following information:

    * *Partition ID*: A unique identifier that identifies the partition. Generated by monotonically incrementation.
    * *Quasi-Identifier*: A list of attributes used to identify the data in the partition.
    * *Split Attribute and Value*: Indicates the attribute and value used to split the partition into children. Useful to search a partition.
    * *Partition Size*: The number of records in the partition.
    * *A<sup>ava</sup>*: A list of remainder attributes available to anonymize.
    * *Children*: The child nodes representing the resulting partitions from the split.

* **Operations:**
The PID Tree supports two main operations:
    * **Partition Search**
    Partition search is performed by traversing the tree from the root until finding the node that contains the searched value. This is achieved by comparing the value with the split attribute in each node. Once the corresponding node is found, the partition ID is returned.

    * **Node Insertion**
    To insert a new node into the PID tree, the parent node available at the current level is found simply by searching for the leftmost leaf node. From the parent, the basic information for the new node is derived, such as the quasi-identifier and partition size. Then, the new node is created and added as a child of the parent node.