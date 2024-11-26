import React,{useState}from "react";
function App(){
  const[name, setName] =useState("shiv");
  return(
    <div>
      <h1>my name is {name}</h1>
      click hear to
      <button onClick={() => setName("ishant x")}>Update Name</button>
      </div>
  );
}
export default App;