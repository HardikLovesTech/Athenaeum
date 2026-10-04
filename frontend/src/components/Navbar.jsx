import {
  BookOpen,
  ChevronDown,
  Search,
} from "lucide-react";

function Navbar() {
  return (
    <header className="Navbar">
      <div className="Brand">
        <BookOpen size={34} strokeWidth={1.8} />

        <div>
          <div className="BrandName">Athenaeum</div>
          <div className="BrandTagline">
            Your Knowledge. Amplified.
          </div>
        </div>
      </div>

      <nav className="Navigation">
        <button className="NavigationItem Active">
          Home
        </button>

        <button className="NavigationItem">
          Documents
        </button>

        <button className="NavigationItem">
          Ask AI
        </button>

        <button className="NavigationItem">
          Summaries
        </button>
      </nav>

      <div className="NavbarRight">
        <div className="SearchBar">
          <Search size={17} />
          <span>Search anything...</span>
          <kbd>⌘ K</kbd>
        </div>

        <div className="Profile">
          <div className="ProfileAvatar">C</div>

          <span>c0d3crusad3r</span>

          <ChevronDown size={15} />
        </div>
      </div>
    </header>
  );
}

export default Navbar 