import { wallet }from "./wallet";
import { TezosToolkit } from "@taquito/taquito";
import { wallet } from "./wallet";
export const tezos= new TezosToolkit("https://jakartanet.smartpy");

tezos.setWalletProvider(wallet);