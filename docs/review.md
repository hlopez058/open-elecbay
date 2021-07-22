


## General Market Process Flow
The market mechanics are going to have different steps based on what state the participant starts in, but the general ones are provided below. The participant is either 
1. Registering on to the maket , 
2. Bidding/Offering before the gate closure (GC)
3. Consuming/Generating energy within the energy exchange period, (where they can be asked to bid additionally for imbalancing service opportunities)


![process_flow](process_flow.svg)

## Billing Mechanisim
After the gate closure for the settlement period. The Billing Mechanisim (BM) is used to evaluet the net imbalance of the transmission system.

![bm_process](bm_process.svg)

## Balancing Services Adjustment Data
Alongside the Billing Mechanisim the Balancing Services are additional bids that are taken from the committed participants to help balance out the grid. The additional offers/bids are done through an auction style system where the broker chooses the best possible solution for the imbalance effort required factoring in safety, time, and price into the equation. 

![bsad_process](bsad_process.svg)

## Settlement Period Contracting

Each settlement cycle consists of interactions between the producer,consumer, and broker. The current process uses a series of bids and offers that are negotated between the producer and consumers resulting in approved contracts by the broker before the gate closure deadline is reached. The submitted contracts are monitored so that any deviation results in the appropriate financial impact as indicated by the balancing authority. The broker also assess the imbalance and looks for additional negotiations with the parties to ammend the contracts as needed to help the imbalance.

![settlement](settlement_process.svg)

## Manage the Imbalance
There is often a disparity between the promised amount of energy in the placed orders and the actual energy consumption as recorded by smart meters. After the settlement process the broker needs to find ways to settle the imbalance. It does so by leveraging different mechanisims during the energy exchange period.  

![balancing_logic](balancing_logic.svg)



## Software Architecture of Open-Elecbay

A proposal for an architecture that handles streaming IoT data sets from multiple clients requesting independent bids/offers on the market. The architecture utilizes MQTT and existing IOT protocol to facilitate a publish/subscribt style of communication. The transactions of the system is brokered and recorded through various microservices. The design can be scaled and distributed across agents. 

![architecture](architecture.svg)