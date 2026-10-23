import TitleLogo from "./TitleLogo";

function Sidebar() {
  return (
    <div className="flex-col w-64 bg-gray-800 text-white rounded-r-lg p-4 h-screen">
      {/* Title - Logo */}
      <TitleLogo />
    </div>
  );
}
export default Sidebar;
