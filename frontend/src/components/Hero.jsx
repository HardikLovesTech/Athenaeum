import {
  ArrowUpRight,
  MessageSquare,
  Upload,
} from "lucide-react";

function Hero() {
  return (
    <section className="Hero">
      <div className="HeroContent">
        <div className="Eyebrow">
          AI-POWERED RESEARCH ASSISTANT
          <span />
        </div>

        <h1>
          Turn your documents
          <br />
          into knowledge.
        </h1>

        <p>
          Upload, explore, ask questions, and get AI-powered insights
          <br />
          from your documents.
        </p>

        <div className="HeroActions">
          <button className="PrimaryButton">
            <Upload size={18} />
            Upload Document
            <ArrowUpRight size={17} />
          </button>

          <button className="SecondaryButton">
            <MessageSquare size={18} />
            Ask AI
            <ArrowUpRight size={17} />
          </button>
        </div>
      </div>

      <div className="HeroVisual">
        <div className="HeroPaper">
          <span>SAME</span>
          <span>DOCUMENTS.</span>
          <span>DEEPER</span>
          <span>INSIGHTS.</span>

          <div className="AccentCircles">
            <span />
            <span />
          </div>
        </div>

        <div className="HeroMountain">
          <div className="MountainShape" />
        </div>
      </div>

      <div className="HeroSideText">
        <span>READ</span>
        <span>ASK</span>
        <span>SUMMARIZE</span>
        <span>DISCOVER</span>

        <div className="HeroDivider" />

        <span>KNOWLEDGE</span>
        <span>MEETS</span>
        <span>INTELLIGENCE</span>

        <div className="HeroDots">
          <i className="ActiveDot" />
          <i />
          <i />
          <i />
        </div>
      </div>
    </section>
  );
}

export default Hero;