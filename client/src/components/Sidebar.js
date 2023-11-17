// Move styles to index.css
import React, { useState } from 'react';
import { Sidebar, SubMenu, Menu, MenuItem } from 'react-pro-sidebar';
// icons
import { RiTeamLine, RiCalendar2Line, RiUserUnfollowLine } from 'react-icons/ri';
import { FiChevronsLeft, FiChevronsRight } from 'react-icons/fi';
import { FaCode, FaUpload} from 'react-icons/fa';
import { Link } from 'react-router-dom'
// css
import 'assets/global.css';

function Sidebars({ onCollapsedChange }) {

  const [collapsed, setCollapsed] = useState(false);
  const [toggled, setToggled] = useState(false);

  const handleCollapsedChange = () => {
    setCollapsed(!collapsed);
    onCollapsedChange(!collapsed); // Notify the parent component about the state change
  };
  const handleToggleSidebar = (value) => {
    setToggled(value);
  };

  return (
    <div style={{ display: "flex" }}>
      <Sidebar
        className={`app ${toggled ? "toggled" : ""}`}
        style={{ height: "100%", position: "absolute", display: "inline-block" }}
        collapsed={collapsed}
        toggled={toggled}
        handleToggleSidebar={handleToggleSidebar}
        handleCollapsedChange={handleCollapsedChange}
      >
        <main>
          <Menu>
            {collapsed ? (
              <MenuItem
                icon={<FiChevronsRight />}
                onClick={handleCollapsedChange}
              ></MenuItem>
            ) : (
              <MenuItem
                suffix={<FiChevronsLeft />}
                onClick={handleCollapsedChange}
                className="menu-item"
              >
                <div className="title">PYTHON TUTOR</div>
              </MenuItem>
            )}
            <hr />
          </Menu>

          <Menu>
          {/* Warning cuz of double <a> can use NavLink, but it breaks submenu */}
            <Link to="/upload">
              <MenuItem icon={<FaUpload />}>
                Odevzdání
              </MenuItem>
            </Link>
            <SubMenu defaultOpen label={"Example"} icon={<RiTeamLine />}>
              <MenuItem icon={<FaCode />}>Regex</MenuItem>
              <MenuItem icon={<RiUserUnfollowLine />}>List</MenuItem>
              <MenuItem icon={<RiCalendar2Line />}>Set</MenuItem>
            </SubMenu>
          </Menu>
        </main>
      </Sidebar>
    </div>
  );
}
export default Sidebars;
