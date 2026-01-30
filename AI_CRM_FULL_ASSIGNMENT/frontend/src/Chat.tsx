
import { useDispatch } from 'react-redux'
import { setInteraction } from './interactionSlice'

export default function Chat(){
 const dispatch = useDispatch()

 async function send(msg:string){
  const res = await fetch('http://localhost:8000/chat',{
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({message:msg})
  })
  const data = await res.json()
  dispatch(setInteraction(data))
 }

 return (
  <div style={{width:'35%',borderLeft:'1px solid #ccc',padding:20}}>
   <h3>AI Assistant</h3>
   <button onClick={()=>send("Today I met with Dr Smith, positive sentiment, shared brochures")}>
    Log Sample Interaction
   </button>
  </div>
 )
}
