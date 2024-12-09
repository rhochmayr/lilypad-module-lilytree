# Lilytree for Lilypad and Docker

## Introduction

Lilytree is a demo module that combines Blender geometry nodes and Blender scripting to generate a customized rendering of a stylized fantasy tree. The project allows you to create a 3D rendering of a procedurally generated tree that is based on inpurt parameters taken from an Ethereum address.

![Lilytree 3D Blender](examples/lilytree_0xb0790aAcE3294d0e0c8892fa2B8a54172449D8B4.jpeg)

## Lilypad

To run Lilytree on the Lilypad network, you can use the following commands:

Defaults:

```sh
lilypad run github.com/rhochmayr/lilypad-module-lilytree:0.0.1
```

Custom ETH Address:

```sh	
lilypad run github.com/rhochmayr/lilypad-module-lilytree:0.0.1 -i ETH_Address="0x0352485f8a3cB6d305875FaC0C40ef01e0C06535"
```

## Docker

### Building and Running the Docker Container

To build and run the Docker container for Lilysay 3D, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/rhochmayr/lilypad-module-lilytree.git
   cd lilypad-module-lilytree
   ```

2. Build the Docker image:
   ```sh
   docker build -t lilytree .
   ```

3. Run the Docker container:
   ```sh
   docker run --rm --gpus all $(pwd)/outputs:/outputs lilytree <eth_address>
   ```

   Replace `<eth address>` with the desired ethereum wallet address you want to use as input parameters for the procedural generation of the tree.

### Usage Instructions

The module depends on the blender scene `/blender-assets/lilytree.blend` and the script `lilytree.py`.

The scene consists of a fantasy tree, lights, camera and geometry nodes.

The script is responsible to convert the specified etherum address into 20 input parameters for the geo-node modifiers of the tree and to trigger the rendering.

1. Ensure you have Blender installed on your system.

2. Run the script with the desired Ethereum address as input:
   ```sh
   blender --background -b "/blender-assets/lilytree.blend" --python "lilytree.py" -- <eth address>
   ```

   Replace `<eth address>` with the desired ethereum wallet address you want to use as input parameters for the procedural generation of the tree.

3. The rendered image will be saved in the `outputs` directory.

### Conversion of Ethereum Address to Input Parameters

The script `lilytree.py` converts an Ethereum address into 20 input parameters for the geo-node modifiers of the tree. Here is how it works:

1. **Extract the Ethereum Address**: The script takes the Ethereum address as a command-line argument.
2. **Remove '0x' Prefix**: If the address starts with '0x', it is removed.
3. **Split into Hex Pairs**: The address (now 40 characters long) is split into 20 groups of 2 characters each.
4. **Convert to Integers**: Each hex pair is converted to an integer (0-255).
5. **Normalize Values**: These integers are then normalized to fit the required ranges for the geo-node modifiers.

#### Example of the Print Outputs

Here is an example of the print outputs from the script showing how the address is broken down into hex pairs and converted into input parameters for the tree generation:

```
eth_address: 0x40B38765696e3d5d8d9d834D8AaD4bB6e418E489

--- Ethereum Address Breakdown ---
Index  Hex Pair   Decimal
--------------------------
[00]   [40]   ->   64
[01]   [B3]   ->   179
[02]   [87]   ->   135
[03]   [65]   ->   101
[04]   [69]   ->   105
[05]   [6e]   ->   110
[06]   [3d]   ->   61
[07]   [5d]   ->   93
[08]   [8d]   ->   141
[09]   [83]   ->   131
[10]   [4D]   ->   77
[11]   [8A]   ->   138
[12]   [aD]   ->   173
[13]   [4b]   ->   75
[14]   [B6]   ->   182
[15]   [e4]   ->   228
[16]   [18]   ->   24
[17]   [E4]   ->   228
[18]   [89]   ->   137
[19]   [48]   ->   72

--- Updating Modifiers Based on Ethereum Address ---
[Base Count]            : 10  (Range: 3-25)
[Tree Seed]             : 700  (Range: 0-1000)
[Trunk Resolution]      : 150  (Range: 8-256)
[Resolution]            : 40  (Range: 8-64)
[Tree Distortion]       : 0.412  (Range: 0.000-1.000)
[Trunk Noise Y]         : 2.500  (Range: -10.000 to 10.000)
[Trunk Noise Z]         : 3.000  (Range: -10.000 to 10.000)
[Split Angle]           : 20.000  (Range: 0.000-45.000)
[Branch Length]         : 2.000  (Range: 1.000-3.000)
[Branch Count]          : 10  (Range: 3-15)
[Branch Seed]           : 500  (Range: 0-1000)
[Leaves Seed]           : 600  (Range: 0-1000)
[Leaves Color R]        : 0.500  (Range: 0.000-1.000)
[Leaves Color G]        : 0.300  (Range: 0.000-1.000)
[Leaves Color B]        : 0.700  (Range: 0.000-1.000)
[Leaves Noise Y]        : 5.000  (Range: -10.000 to 10.000)
[Leaves Noise Z]        : 6.000  (Range: -10.000 to 10.000)
[Vines Toggle]          : True
[Vine Gravity]          : -2.500  (Range: -5.000 to 0.000)
[Vine Seed]             : 800  (Range: 0-1000)
```

## Dependencies and Credits

- Blender: https://www.blender.org/
- Tree Gen v1.1: https://rc12.gumroad.com/l/fantasytree