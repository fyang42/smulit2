# prompts/main.py

from prompts.automata import AutomataTemplate
from prompts.smart_contract import SmartContractTemplate
from prompts.vuln import VulnerabilityTemplate

# Automata Theory in Smart Contracts
automata_prompt = AutomataTemplate()
fsm_description = automata_prompt.format(fsm_details="Include specific FSM logic or special conditions.")
print("FSM Description:\n", fsm_description)

# Smart Contract Generation
smart_contract_prompt = SmartContractTemplate()
generated_code = smart_contract_prompt()
print("Generated Smart Contract:\n", generated_code)

# Vulnerability Analysis
vulnerability_prompt = VulnerabilityTemplate()
contract_code = """
contract Auction {
    address public highestBidder;
    uint public highestBid;
    mapping(address => uint) pendingReturns;
    bool ended;

    function bid() public payable {
        require(msg.value > highestBid, "There already is a higher bid.");
        if (highestBid != 0) {
            pendingReturns[highestBidder] += highestBid;
        }
        highestBidder = msg.sender;
        highestBid = msg.value;
    }

    function withdraw() public returns (bool) {
        uint amount = pendingReturns[msg.sender];
        if (amount > 0) {
            pendingReturns[msg.sender] = 0;
            if (!payable(msg.sender).send(amount)) {
                pendingReturns[msg.sender] = amount;
                return false;
            }
        }
        return true;
    }

    function auctionEnd() public {
        require(!ended, "auctionEnd has already been called.");
        ended = true;
        payable(highestBidder).transfer(highestBid);
    }
}
"""
vulnerability_analysis = vulnerability_prompt(contract_code=contract_code)
print("Vulnerability Analysis:\n", vulnerability_analysis)
