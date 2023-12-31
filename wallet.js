import { BeaconWallet } from "@taquito/taquito";

export const wallet = new BeaconWallet({
    name:"Tezos Toss  Game",
    preferredNetwork:""
});
export const connectWallet = async ()=>{
    await wallet.requestPermissions({network:{type:"jakartanet"}});
};
export const getAccount = async ()=>{
    const activeAccount=await wallet.client.getActiveAccount();
    if(activeAccount){
        return activeAccount.address;
    }
    else{ 
        return "";
    }
};
