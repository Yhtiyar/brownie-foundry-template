# Brownie x Foundry Template

Template repository for getting started quickly with Brownie and Foundry in one project
Inspired by [hardhat-foundry-template](https://github.com/foundry-rs/hardhat-foundry-template)

## Getting Started

Click [`use this template`](https://github.com/Yhtiyar/brownie-foundry-template/generate) to create a new repository with this repo as the initial state.

- Use Foundry:

```bash
forge install
forge test
```

- Use Brownie:

```bash
brownie test
```

## Features

- Write / run tests with either Brownie or Foundry:

  ```
  forge test
  # or
  brownie test
  ```

- Install libraries with Foundry which work with Brownie:

  1. Install with forge:

  ```bash
  forge install openzeppelin=https://github.com/OpenZeppelin/openzeppelin-contracts
  ```

  2. Print foundry remappings:

  ```bash
  forge remappings >> remappings.txt
  ```

  3. Update remappings in `brownie-config.yaml`

- Generate CLI and Python interface to the smart contracts with [moonworm](https://github.com/bugout-dev/moonworm). See [utils/README.md](utils/README.md) for more details.
