import { useEffect, useState} from "react";
import { connectWallet, getAccount } from "../utils/wallet";

const Navbar= () => {
    const [account, setAccount] = useState("");

    useEffect(() => {
        (async () => {
        setAccount("");
    })();
}, []);

const onConnectWallet = async() => {
    await connectWallet();
    const activeAccount= await getAccount();
    setAccount (activeAccount);
};
return (
    <div className="navbar navbar-dark bg-dark fixed top">
        <div className="container py-2">
            <a href="/" className="navbar-round">
                Tezos Lottery
            </a>
            <div className="d-flex">
                {
                    <button onClick ={onConnectWallet} className="btn btn-outline-info">
                        {}
                        Connect Wallet
                    </button>
                }
            </div>
        </div>
    </div>
   );  
};
export default Navbar
    