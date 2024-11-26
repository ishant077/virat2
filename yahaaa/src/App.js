import { Fragment } from "react"; 
import React from 'react'; 
function Student (props){ 
 return ( 
 <div> 
 <h1> 
 Name:{props.name} 
 </h1> 
 <p> 
 Marks:{props.marks} 
 </p> 
 </div> 
 ) 
} 
function App(){ 
 return ( 
 <Fragment> 
 <Student name={"abhi"} marks={90}/> 
 </Fragment> 
 ) 
} 
export default App;