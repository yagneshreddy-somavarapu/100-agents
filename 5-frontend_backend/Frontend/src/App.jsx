import { useState, useRef, useEffect, use } from "react";
import axios from 'axios';
import LLMResponse from "./LLMResponse";
function App() {
  const [value, setValue] = useState("");
  const textareaRef = useRef(null);
  let [data,setData]=useState([])
  let [loading,setLoading] = useState(false)

  useEffect(() => {
    const textarea = textareaRef.current;
    if (!textarea) return;

    textarea.style.height = "auto";
    textarea.style.width = "auto";

    const newHeight = Math.min(textarea.scrollHeight, 120);
    textarea.style.height = newHeight + "px";

    const newWidth = Math.min(textarea.scrollWidth, 300);
    textarea.style.width = newWidth + "px";
  }, [value]);

  const handleSubmit = (e) => {
    e.preventDefault();
    setLoading(true)
    if (!value.trim()) return;
    setData((pre) => [...pre, { "user": "User", "content": value.trim() }])
    axios.post("http://127.0.0.1:8000/Agent",{
      "user_input" : value.trim()
    }).then((res) => { 
      setData((pre) => [...pre, { "user": "Agent", "content": res.data.response }])
      setLoading(false)
   })
      .catch((err) => {
        setLoading(true)
        alert(`Server is Bussey Right Now Resion : ${err}`)
  })

    setValue(""); 
    textareaRef.current.focus(); 
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  return (
    <div className="flex">
      <div className="h-screen w-screen bg-[#080808] text-white flex flex-col justify-between items-center">
        <div className="w-full bg-black p-3 pl-10 text-xl font-bold border-[#2E2E2E] border-b-[0.1px]">
          <p>Agent</p>
        </div>

        <div className="w-screen h-screen pl-50 pt-10 pr-50 pb-25 overflow-y-auto scroll-hidden flex flex-col gap-4" 
        style={{
          scrollbarWidth: 'thin',
          scrollbarColor: '#555 #1a1a1a',
        }}>
          {
            data.map((item, index) => (
              <div
                key={index}
                className={`w-full flex ${item.user === 'Agent' ? 'justify-start' : 'justify-end'} mb-2`}
              >
                <div
                  className={`rounded-lg max-w-[70%] break-words ${item.user === 'agent' ? '' : 'bg-[#333232]'
                    } inline-block`}
                > 

                  {/* {item.content} */}
                  <LLMResponse data={item.content}/>
                </div> 
              </div>
            ))
          }

        </div>

        <form
          onSubmit={handleSubmit}
          className="w-[50%] bg-[#333232] fixed top-165 text-white p-3 rounded-[50px] mb-10 flex justify-between gap-4"
        >
          <textarea
            ref={textareaRef}
            disabled={loading}
            value={value}
            onChange={(e) => setValue(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder={loading ?"Loading......": "Type your message..."}
            rows={1}
            className="resize-none outline-none pl-10 w-[95%] h-8 overflow-hidden bg-transparent"
          />
          <button
            type="submit"
            className="cursor-pointer scale-[1.5] pr-4 rounded-[100px]"
          >
           {loading ? "": "⬆️"}
          </button>
        </form>
      </div>
    </div>
  );
}

export default App;
