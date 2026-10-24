import TitleLogo from "./TitleLogo";
import Nav from "./Nav";

function Sidebar() {
  return (
    <div className="flex-col w-64 bg-gray-100 border-r border-mist-500 p-4 shrink-0">
      {/* Title - Logo */}
      <TitleLogo />
      {/* Nav links */}
      <Nav />
    </div>
  );
}
export default Sidebar;
