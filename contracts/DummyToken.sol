// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
import "openzeppelin/token/ERC20/ERC20.sol";

contract DummyToken is ERC20 {
    constructor() ERC20("DummyToken", "DMT") {
        _mint(msg.sender, 1000000000000000000000000);
    }
}
