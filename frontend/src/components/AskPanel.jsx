import {
    BookOpen, 
    ChevronDown,
    Send,
    Sparkles,
} from "lucide-react";


import SourceCard from "./SourceCard";

function AskPanel() {
    return (
        <section className="AskPanel">
            <div className="AskHeader">
                <div>
                    <h2>
                        <Sparkles size={22} />
                        Ask your documents
                    </h2>
                </div>

                <div className="PoweredBy">
                    POWERED BY AI
                    <br/>
                    GROUNED IN YOUR KNOWLEDGE
                </div>
            </div>

            <div className="DocumentSelector">
                <div className="PdfIcon">PDF</div>

                <span>AWS Cloud Practitioner.pdf</span>

                <ChevronDown size={17} />

            </div>

            <div className="QuestionBox">
                <span>What is AWS Cloud Practitioner?</span>
                <button className="SendButton">
                    <Send size={17} />
                </button>
            </div>


            <div className="PromptChips">
                <button>Summarize this document</button>
                <button>Key Concepts</button>
                <button>Exam topics</button>
            </div>

            <div className="AnswerCard">
                <div className="AnswerHeader">
                    <h3>
                        <span className="AiIcon"/>
                        Answer
                    </h3>
                
                    <span>Just now</span>
                
                </div>
                <p>
                AWS Cloud Practitioner is an entry-level certification from Amazon Web Services (AWS) that validates a foundational understanding of cloud concepts, AWS services, security, pricing, and support. It is designed for individuals who are new to cloud computing and provides a broad overview of how AWS works, including core services, the shared responsibility model, and basic architectural principles.
                </p>

                <div className="Sources">
                    <div className="SourcesHeader">
                        <span>
                            <BookOpen size={16} />
                            Sources (2)
                        </span>

                        <button>View in document</button>
                    </div>
                    <SourceCard
                        Chunk="Chunk 0"
                        Relevance="0.18"
                        Text="The AWS Certified Cloud Practitioner validates a foundational..."
                    />

                    <SourceCard
                        Chunk="Chunk 3"
                        Relevance="0.24"
                        Text="This certification is designed for indivisuals whe are new to ..."
                    />


                </div>

            </div>

        </section>
    )
}



export default AskPanel;