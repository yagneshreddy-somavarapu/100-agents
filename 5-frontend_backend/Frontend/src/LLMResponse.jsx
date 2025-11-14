import React from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeHighlight from "rehype-highlight";
import "highlight.js/styles/github.css"; // or choose any highlight.js theme

const LLMResponse = ({ data }) => {
    return (
        <div className="text-white shadow-md rounded-xl pt-2 pb-1 pl-5 pr-5 max-w-3xl mx-auto">
            <ReactMarkdown
                children={data}
                remarkPlugins={[remarkGfm]}
                rehypePlugins={[rehypeHighlight]}
                components={{
                    h1: ({ node, ...props }) => <h1 className="text-2xl font-bold mt-4 mb-2" {...props} />,
                    h2: ({ node, ...props }) => <h2 className="text-xl font-semibold mt-3 mb-2" {...props} />,
                    p: ({ node, ...props }) => <p className="text-gray-300 leading-relaxed mb-2" {...props} />,
                    ul: ({ node, ...props }) => <ul className="list-disc ml-6 mb-2" {...props} />,
                    ol: ({ node, ...props }) => <ol className="list-decimal ml-6 mb-2" {...props} />,
                    code: ({ node, inline, className, children, ...props }) => (
                        <code
                            className={`bg-gray-100 text-black mt-4 mb-4 p-4 rounded px-1 ${inline ? "text-sm" : "block p-4 overflow-x-auto"}`}
                            {...props}
                        >
                            {children}
                        </code>
                    ),
                }}
            />
        </div>
    );
};

export default LLMResponse;
