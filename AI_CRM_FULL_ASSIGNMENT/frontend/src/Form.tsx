
import { useSelector } from 'react-redux'

export default function Form(){
 const data:any = useSelector((s:any)=>s.interaction)
 return (
  <div style={{width:'65%',padding:20,overflowY:'scroll'}}>
   <h2>Log HCP Interaction</h2>
   <input disabled value={data.hcp_name||''} placeholder="HCP Name"/>
   <textarea disabled value={data.topics||''} placeholder="Topics Discussed"/>
   <p>Sentiment: {data.sentiment}</p>
  </div>
 )
}
